import pytest
from playwright.sync_api import Page

from pages.brand_page import BrandPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage


@pytest.fixture
def catalog_page(chromium_page: Page) -> CatalogPage:
    return CatalogPage(page=chromium_page)

@pytest.fixture
def product_page(chromium_page: Page) -> ProductPage:
    return ProductPage(page=chromium_page)

@pytest.fixture
def brand_page(chromium_page: Page) -> BrandPage:
    return BrandPage(page=chromium_page)