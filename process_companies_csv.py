import asyncio
import pandas as pd
from playwright.async_api import async_playwright, Error
import logging

logger = logging.getLogger(__name__)


async def get_linkedin_urls(csv_file):
    data = pd.read_csv(csv_file)
    df = pd.DataFrame(data, columns=['companies'])
    df['linkedin_url'] = None  # Add a new column for LinkedIn URLs

    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
            context = await browser.new_context()

            tasks = []
            for index, row in df.iterrows():
                company_name = row['companies']
                page = await context.new_page()
                task = fetch_linkedin_url_for_company(page, company_name, index, df)
                tasks.append(task)

            await asyncio.gather(*tasks)
        except Exception as e:
            logger.error(f"Error occurred: {e}", exc_info=True)
        finally:
            await context.close()
            await browser.close()

    return df


async def fetch_linkedin_url_for_company(page, company_name, index, df):
    try:
        await page.goto(f"https://www.linkedin.com/company/{company_name}")
        linkedin_url = page.url
        df.at[index, 'linkedin_url'] = linkedin_url
    except Error as e:
        print(f"Error occurred: {str(e)}")
    finally:
        await page.close()
