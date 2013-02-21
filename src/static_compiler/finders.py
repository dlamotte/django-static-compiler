from __future__ import absolute_import

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.files.storage import FileSystemStorage
from static_compiler.storage import StaticCompilerFileStorage


class StaticCompilerFinder(finders.BaseStorageFinder):
    """
    A staticfiles finder that looks in the compiler's cache directory
    for intermediate files.
    """
    storage = StaticCompilerFileStorage

    def list(self, ignore_patterns):
        filesystem_storage = FileSystemStorage(location=settings.STATIC_ROOT)
        for pkg in settings.STATIC_BUNDLES['packages'].keys():
            yield pkg, filesystem_storage
