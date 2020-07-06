from importlib import import_module


def import_icon_set(icon_set: str):
    icon_set_str = icon_set
    asset_path = f'ada_hub.lib.gui.assets.icon_sets.{icon_set_str}.icons'
    icons = import_module(asset_path)

    return icons
