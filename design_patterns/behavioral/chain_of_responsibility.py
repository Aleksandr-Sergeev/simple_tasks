from abc import ABC, abstractmethod
from typing import Any


class AbstractCompCheck(ABC):
    @abstractmethod
    def set_next(self, next: Any):
        pass

    @abstractmethod
    def handle(self, request: dict):
        pass


class BaseCompCheck(AbstractCompCheck):
    _next_comp_check: AbstractCompCheck = None

    def set_next(self, next: AbstractCompCheck):
        self._next_comp_check = next
        return next

    @abstractmethod
    def handle(self, request: dict) -> bool:
        if self._next_comp_check:
            return self._next_comp_check.handle(request)
        return True


class CPUCheck(BaseCompCheck):

    def handle(self, request: dict):
        stat = request.get('stat')
        stat = stat if stat else {}
        cpu = request.get('cpu')
        stat['cpu'] = cpu
        cpu_check = True if cpu and cpu != "" else False
        return super(CPUCheck, self).handle(request) if cpu_check else False


class RAMCheck(BaseCompCheck):

    def handle(self, request: dict):
        stat = request.get('stat')
        stat = stat if stat else {}
        ram = request.get('ram')
        stat['ram'] = ram
        ram_check = True if ram and ram != "" else False
        return super(RAMCheck, self).handle(request) if ram_check else False


if __name__ == '__main__':
    cpu_check = CPUCheck()
    ram_check = RAMCheck()
    cpu_check.set_next(ram_check)

    sample_request = {
        'cpu': 'intel',
        'ram': 'GDDR5',
    }

    cpu_check.handle(request=sample_request)
