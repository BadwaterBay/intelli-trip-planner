#!/usr/bin/env python

"""
# Call National Park Services (NPS) API
"""

import os
import asyncio
from dotenv import load_dotenv
import httpx


NPS_API_URL_BASE = "https://developer.nps.gov/api/v1"
RESULTS_PER_PAGE = 50


def compose_url_nps_visitor_centers(park_code, page_number=0) -> str:
    return (
        NPS_API_URL_BASE
        + "/visitorcenters"
        + "?parkCode="
        + park_code
        + "&start="
        + str(page_number * RESULTS_PER_PAGE)
        + "&limit="
        + str(RESULTS_PER_PAGE)
    )


def compose_url_nps_activities(park_code, page_number=0) -> str:
    return (
        NPS_API_URL_BASE
        + "/activities"
        + "?parkCode="
        + park_code
        + "&start="
        + str(page_number * RESULTS_PER_PAGE)
        + "&limit="
        + str(RESULTS_PER_PAGE)
    )


def compose_url_nps_campgrounds(park_code, page_number=0) -> str:
    return (
        NPS_API_URL_BASE
        + "/campgrounds"
        + "?parkCode="
        + park_code
        + "&start="
        + str(page_number * RESULTS_PER_PAGE)
        + "&limit="
        + str(RESULTS_PER_PAGE)
    )


async def call_nps_api_with_get(url_get, park_code, api_key, page_number=0) -> list:
    headers_nps = {"X-Api-Key": api_key}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url_get(park_code, page_number), headers=headers_nps
        )

    if response.status_code != 200:
        raise Exception(response.status_code)

    response_json = response.json()
    if len(response_json.get("data")) < RESULTS_PER_PAGE:
        return response_json.get("data")

    page_number += 1
    return response_json.get("data") + await call_nps_api_with_get(
        url_get, park_code, api_key, page_number
    )


async def main() -> list:
    # Example park codes:
    # - Death Valley: deva
    # - Zion: zion

    load_dotenv()
    api_key = os.environ.get("API_KEY_NPS")
    response = await call_nps_api_with_get(compose_url_nps_activities, "deva", api_key)
    print(response)
    print(len(response))
    return response


if __name__ == "__main__":
    asyncio.run(main())
