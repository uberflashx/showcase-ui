import pytest
from playwright.sync_api import Page

from pages.brand_page import BrandPage
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage


@pytest.fixture
def catalog_page(page: Page) -> CatalogPage:
    return CatalogPage(page=page)

@pytest.fixture
def product_page(page: Page) -> ProductPage:
    return ProductPage(page=page)

@pytest.fixture
def brand_page(page: Page) -> BrandPage:
    return BrandPage(page=page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page=page)