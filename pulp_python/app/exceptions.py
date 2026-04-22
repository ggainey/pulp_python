from gettext import gettext as _

from pulpcore.plugin.exceptions import PulpException


class AttestationVerificationError(PulpException):
    """
    Raised when attestation verification fails.
    """

    error_code = "PYT0001"

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"[{self.error_code}] " + _("Attestation verification failed: {message}").format(
            message=self.message
        )


class UnsupportedProtocolError(PulpException):
    """
    Raised when an unsupported protocol is used for syncing.
    """

    error_code = "PYT0002"

    def __init__(self, protocol):
        super().__init__()
        self.protocol = protocol

    def __str__(self):
        return f"[{self.error_code}] " + _(
            "Only HTTP(S) is supported for python syncing, got: {protocol}"
        ).format(protocol=self.protocol)


class InvalidAttestationsError(PulpException):
    """
    Raised when attestation data cannot be validated.
    """

    error_code = "PYT0003"

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"[{self.error_code}] " + _("Invalid attestations: {message}").format(
            message=self.message
        )
