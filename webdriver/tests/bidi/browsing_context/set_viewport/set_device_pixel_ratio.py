import pytest

from ... import get_device_pixel_ratio, get_viewport_dimensions


@pytest.mark.asyncio
@pytest.mark.parametrize("device_pixel_ratio", [1, 2])
async def test_set_device_pixel_ratio(bidi_session, new_tab, device_pixel_ratio):
    await bidi_session.browsing_context.set_viewport(
        context=new_tab["context"],
        device_pixel_ratio=device_pixel_ratio)

    assert await get_device_pixel_ratio(bidi_session, new_tab) == device_pixel_ratio


@pytest.mark.asyncio
@pytest.mark.parametrize("device_pixel_ratio", [1, 2])
async def test_set_viewport_with_dpr(bidi_session, new_tab, device_pixel_ratio):
    test_viewport = {"width": 250, "height": 300}

    await bidi_session.browsing_context.set_viewport(
        context=new_tab["context"],
        viewport=test_viewport,
        device_pixel_ratio=device_pixel_ratio)

    assert await get_viewport_dimensions(bidi_session, new_tab) == test_viewport
    assert await get_device_pixel_ratio(bidi_session, new_tab) == device_pixel_ratio


@pytest.mark.asyncio
async def test_unset_device_pixel_ratio(bidi_session, new_tab):
    original_dpr = await get_device_pixel_ratio(bidi_session, new_tab)
    test_dpr = original_dpr + 1

    await bidi_session.browsing_context.set_viewport(
        context=new_tab["context"],
        device_pixel_ratio=test_dpr)

    assert await get_device_pixel_ratio(bidi_session, new_tab) == test_dpr

    await bidi_session.browsing_context.set_viewport(
        context=new_tab["context"],
        device_pixel_ratio=None)

    assert await get_device_pixel_ratio(bidi_session, new_tab) == original_dpr
