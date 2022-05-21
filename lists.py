from urllib import request
sample_videos_csv = 'https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url =r'sample.csv'
    fw = open(dest_url, "w")
    for line in lines:
        fw.write(line + "\n")
    fw.close()

download_stock_data(sample_videos_csv)

