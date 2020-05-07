from . import AbstractRemoteHostDriver, AbstractShareableDeviceDriver, AbstractLocalDriver, AbstractCommunicator


class MockDriverMetaData(object):
    SUPPORTED_COMMUNICATORS = ('MockCommunicator',)
    SUPPORTED_HOST_TYPES = ('Linux_AMD64',)


class MockHost(AbstractRemoteHostDriver, MockDriverMetaData):
    IDENTIFIER = 'MockHost'

    @property
    def is_reachable(self) -> bool:
        return True

    def update_device_states(self, devices):
        return None


class MockDevice(AbstractShareableDeviceDriver, MockDriverMetaData):
    IDENTIFIER = 'MockDevice'

    def start_sharing(self, **kwargs):
        return

    def stop_sharing(self):
        return

    def get_share_state(self):
        return True

    def get_online_state(self):
        return True


class MockLocal(AbstractLocalDriver):
    IDENTIFIER = 'MockLocal'

    def connect(self):
        pass

    def disconnect(self):
        pass

    def connected(self) -> bool:
        pass

    def setup_information(self) -> str:
        return "No setup needed for Mock Driver"


class MockCommunicator(AbstractCommunicator):
    IDENTIFIER = 'MockCommunicator'
    pass


################################################################################
#
# This is being done to prevent circular dependencies
MockDevice.HOST_CLASS = MockHost
MockHost.DEVICE_CLASS = MockDevice
