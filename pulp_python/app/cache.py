from pulpcore.plugin.cache import CacheKeys, SyncContentCache
from pulpcore.plugin.util import cache_key

ACCEPT_HEADER_KEY = "accept_header"


class PythonApiCache(SyncContentCache):
    """
    Cache for the Simple API.

    Adds Accept header to the cache key so HTML and JSON responses are cached separately.
    """

    def __init__(self, base_key=None):
        keys = (CacheKeys.path, CacheKeys.method, ACCEPT_HEADER_KEY)
        super().__init__(base_key=base_key, keys=keys)

    def make_key(self, request):
        all_keys = {
            CacheKeys.path: request.path,
            CacheKeys.method: request.method,
            ACCEPT_HEADER_KEY: request.headers.get("accept", ""),
        }
        return ":".join(all_keys[k] for k in self.keys)


def find_base_path_cached(request, cached):
    """
    Resolve the distribution base_path for use as the Redis cache base_key.
    """
    path = request.resolver_match.kwargs["path"]
    return cache_key(path)
