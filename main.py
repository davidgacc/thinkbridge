import logging
import asyncio
import argparse
from process_companies_csv import get_linkedin_urls

logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(description='LinkedIn Scraper')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('output_csv_file', help='Path to the output CSV file')
    return parser.parse_args()


async def main():
    args = parse_arguments()
    csv_file = args.csv_file
    output_csv_file = args.output_csv_file

    try:
        df_companies_url = await get_linkedin_urls(csv_file)
        df_companies_url.to_csv(output_csv_file, index=False)
        logger.info("csv generated successfully")
    except Exception as e:
        logger.error(f"Error occurred: {e}", exc_info=True)

asyncio.run(main())
