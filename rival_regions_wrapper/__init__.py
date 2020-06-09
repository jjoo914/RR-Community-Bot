
"""
Rival Regions Wrapper

This unofficial API wrapper is an implementation
of some Rival Regions functionalities.
"""

from .authentication_handler import AuthenticationHandler
from .middleware import LocalAuthentication, RemoteAuthentication
from .api_wrapper import Profile, Storage, Market, ResourceState, Perks, Craft, Overview, War, \
    Work, Article
