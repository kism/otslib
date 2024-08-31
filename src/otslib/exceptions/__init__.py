class LyricsUnavailableException(Exception):
    """
    Exception raised when a lyrics could not be found for a given song
    """
    pass


class TrackUnavailableException(Exception):
    """
    Exception raised when a track is not available
    """
    pass


class MediaFetchInterruptedException(Exception):
    """
    Exception raised when a media fetch is interrupted by external or internal events/errrs
    """
    pass


class ThumbnailUnavailableException(Exception):
    """
    Exception raised when a media item has no thumbnail associated with it
    """
    pass


class UnknownMediaTypeException(Exception):
    """
    Exception raised when an unknown/unsupported media type is used
    """
    pass


class UnplayableMediaException(Exception):
    """
    Exception raised when an media stream could not be fetched or played back due to it being unlisted or region
    restricted
    """
    pass


class StreamReadException(Exception):
    """
    Exception raised when an error occurs while reading the a spotify media stream
    """
    pass


class InvalidCredentialException(Exception):
    """
    Exception raised when invalid login credentials are used
    """
    pass


class UnknownURLTypeException(Exception):
    """
    Exception raised when an unknown url type is used during a URL classification
    """
    pass


class PremiumRequiredException(Exception):
    """
    Exception raised when an action requires premium spotify account
    """

class TrackNotInPlaylistException(Exception):
    """
    Exception raised when a action to a track for playlist is done when it's not in playlist'
    """
