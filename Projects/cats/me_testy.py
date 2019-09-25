from typing import swap_diff, autocorrect
import tests.construct_check as test
print([swap_diff('succi', 'skcvi', k) > k for k in range(5)])
