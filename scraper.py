import requests
from bs4 import BeautifulSoup
import html2text
import time
import os
import json
import re
import sys
from urllib.parse import urlparse
from pathlib import Path
import subprocess

SITEMAP_INDEX = "https://docs.aws.amazon.com/sitemap_index.xml"
ROBOTS_DISALLOW = [
    "/AmazonCloudFront/2008-06-30/",
    "/AmazonCloudFront/2009-04-02/",
    "/AmazonCloudFront/2009-09-09/",
    "/AmazonCloudFront/2009-12-01/",
    "/AmazonCloudFront/2010-03-01/",
    "/AmazonCloudFront/2010-05-01/",
    "/AmazonCloudFront/2010-06-01/",
    "/AmazonCloudFront/2010-07-15/",
    "/AmazonCloudFront/2010-08-01/",
    "/AmazonCloudFront/2010-11-01/",
    "/AmazonCloudFront/2012-03-15/",
    "/AmazonCloudFront/2012-05-05/",
    "/AmazonCloudFront/2012-07-01/",
    "/AmazonCloudFront/2013-05-12/",
    "/AmazonCloudFront/2013-08-26/",
    "/AmazonCloudFront/2013-09-27/",
    "/AmazonCloudFront/2013-11-11/",
    "/AmazonCloudFront/2013-11-22/",
    "/AmazonCloudFront/2014-01-31/",
    "/AmazonCloudFront/2014-05-31/",
    "/AmazonCloudFront/2014-08-31/",
    "/AmazonCloudFront/2014-10-21/",
    "/AmazonCloudFront/2014-11-06/",
    "/AmazonCloudFront/2015-04-17/",
    "/AmazonCloudWatch/2009-05-15/",
    "/AutoScaling/2009-05-15/",
    "/AWSEC2/2006-06-26/",
    "/AWSEC2/2006-10-01/",
    "/AWSEC2/2007-01-03/",
    "/AWSEC2/2007-01-19/",
    "/AWSEC2/2007-03-01/",
    "/AWSEC2/2007-08-29/",
    "/AWSEC2/2008-02-01/",
    "/AWSEC2/2008-05-05/",
    "/AWSEC2/2008-08-08/",
    "/AWSEC2/2008-12-01/",
    "/AWSEC2/2009-03-01/",
    "/AWSEC2/2009-04-04/",
    "/AWSEC2/2009-07-15/",
    "/AWSEC2/2009-08-15/",
    "/AWSEC2/2009-10-31/",
    "/AWSEC2/2009-11-30/",
    "/AWSEC2/2010-06-15/",
    "/AWSEC2/2010-08-31/",
    "/AmazonVPC/2009-07-15/",
    "/AmazonVPC/2010-06-15/",
    "/AmazonVPC/2010-08-31/",
    "/AWSECommerceService/20070716/",
    "/AWSECommerceService/20071029/",
    "/AWSECommerceService/20080303/",
    "/AWSECommerceService/20080407/",
    "/AWSECommerceService/20080626/",
    "/AWSECommerceService/20080628/",
    "/AWSECommerceService/20080819/",
    "/AWSECommerceService/20090106/",
    "/AWSECommerceService/20091101/",
    "/AWSECommerceService/20100601/",
    "/AmazonFPS/20070108/",
    "/AWSFWS/1.0/",
    "/AWSMechTurk/20070621/",
    "/AWSMechTurk/20080214/",
    "/AWSMechTurk/20080401/",
    "/AWSMechTurk/20070312/",
    "/AWSMechTurk/20061031/",
    "/AWSMechTurk/20060927/",
    "/AmazonSimpleDB/2007-11-07/",
    "/AmazonSimplePay/2007-01-08/",
    "/AWSSimpleQueueService/20060401/",
    "/AWSSimpleQueueService/20070501/",
    "/AWSSimpleQueueService/20080101/",
    "/AmazonFPS/2007-01-08/",
    "/AWSImportExport/2009-12-02/",
    "/AWSImportExport/2009-09-30/",
    "/AWSImportExport/2009-07-28/",
    "/AWSImportExport/2009-05-19/",
    "/AWSImportExport/2009-05-20/",
    "/AWSImportExport/2009-08-13/",
    "/AmazonRDS/2012-04-23/",
    "/AmazonRDS/2012-01-15/",
    "/AmazonRDS/2011-12-19/",
    "/AmazonRDS/2011-04-01/",
    "/AmazonRDS/2010-07-28/",
    "/AmazonRDS/2010-06-28/",
    "/AmazonRDS/2010-01-01/",
    "/AmazonRDS/2009-10-16/",
    "/ElasticLoadBalancing/2010-07-01/",
    "/ElasticLoadBalancing/2009-05-15/",
    "/elastictranscoder/2012-09-25/",
    "/Route53/2010-10-01/",
    "/Route53/2013-04-01/",
    "/awsaccountbilling/latest/about",
    "/cloudhsm/classic/",
    "/forms/",
    "/en_pv/",
    "/freertos/archive/",
    "/iot-expresslink/archive/",
    "/help-panel/",
    "/search/",
]
CRAWL_DELAY = 5  # seconds

# Configure conversion
converter = html2text.HTML2Text()
converter.ignore_links = False
converter.ignore_images = True
converter.ignore_emphasis = False
converter.body_width = 0  # no wrapping

def is_disallowed(url):
    """Return True if the URL path matches any robots.txt Disallow rule."""
    parsed = urlparse(url)
    path = parsed.path
    for dis_path in ROBOTS_DISALLOW:
        if path.startswith(dis_path):
            return True
    return False

def safe_filename(sitemap_url):
    """Create a safe .md filename from a sitemap URL."""
    parsed = urlparse(sitemap_url)
    parts = [p for p in parsed.path.split('/') if p] + [parsed.query if parsed.query else '']
    name = '_'.join(parts[-2:]).replace('?', '_').replace('=', '_')
    name = re.sub(r'[^a-zA-Z0-9_\-]', '_', name)
    return f"{name}.md"

def fetch_sitemap_urls(sitemap_url):
    """Return list of page URLs from a sub-sitemap."""
    resp = requests.get(sitemap_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, 'xml')
    urls = []
    for loc in soup.find_all('loc'):
        url = loc.text.strip()
        if not is_disallowed(url):
            urls.append(url)
    return urls

def scrape_page(url):
    """Fetch page HTML and convert to markdown."""
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    main = soup.find('main') or soup.find('div', id='main-content') or soup.find('body')
    if main:
        html_content = str(main)
    else:
        html_content = resp.text
    return converter.handle(html_content)

def process_sitemap(sitemap_url, repo_dir):
    """Process one sub-sitemap: scrape all pages and write one .md file."""
    print(f"Processing sitemap: {sitemap_url}")
    try:
        page_urls = fetch_sitemap_urls(sitemap_url)
    except Exception as e:
        print(f"Failed to fetch sitemap {sitemap_url}: {e}")
        return False

    if not page_urls:
        print("No allowed pages found.")
        return True

    print(f"Found {len(page_urls)} pages to scrape.")
    markdown_parts = []
    for i, page_url in enumerate(page_urls, 1):
        print(f"  [{i}/{len(page_urls)}] Scraping {page_url}")
        try:
            md = scrape_page(page_url)
            markdown_parts.append(f"# Page: {page_url}\n\n{md}\n\n---\n")
            time.sleep(CRAWL_DELAY)
        except Exception as e:
            print(f"    Error: {e}")
            markdown_parts.append(f"# Page: {page_url}\n\n*Error scraping this page: {e}*\n\n---\n")

    filename = safe_filename(sitemap_url)
    file_path = os.path.join(repo_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(''.join(markdown_parts))
    print(f"Saved {filename}")
    return True

def git_commit_and_push(repo_dir, message):
    """Commit and push changes in repo_dir."""
    os.chdir(repo_dir)
    subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', 'add', '.'], check=True)
    result = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True)
    if result.returncode != 0:
        subprocess.run(['git', 'commit', '-m', message], check=True)
        subprocess.run(['git', 'push'], check=True)
    else:
        print("No changes to commit.")

def main():
    repo_dir = os.environ.get('GITHUB_WORKSPACE', os.getcwd())
    progress_file = os.path.join(repo_dir, 'progress.json')

    # Load existing progress
    completed = []
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            data = json.load(f)
            completed = data.get('completed', [])

    # Fetch all sub-sitemaps from the index
    print("Fetching sitemap index...")
    resp = requests.get(SITEMAP_INDEX)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, 'xml')
    all_sitemaps = []
    for sitemap_tag in soup.find_all('sitemap'):
        loc = sitemap_tag.find('loc')
        if loc:
            all_sitemaps.append(loc.text.strip())

    # Filter already completed
    remaining = [sm for sm in all_sitemaps if sm not in completed]
    print(f"Total sub-sitemaps: {len(all_sitemaps)}, already completed: {len(completed)}, remaining: {len(remaining)}")

    if not remaining:
        print("All sub-sitemaps are already processed!")
        return

    for i, sitemap_url in enumerate(remaining, 1):
        print(f"\n=== Sub-sitemap {i}/{len(remaining)} ===")
        success = process_sitemap(sitemap_url, repo_dir)
        if success:
            completed.append(sitemap_url)
            with open(progress_file, 'w') as f:
                json.dump({'completed': completed}, f)
            git_commit_and_push(repo_dir, f"Processed sitemap: {sitemap_url}")
        else:
            print(f"Failed to process {sitemap_url}, stopping.")
            break

if __name__ == '__main__':
    main()
