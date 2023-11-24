import pytest
from morse import decode


@pytest.mark.parametrize(
    "source_string, result",
    [
        ("... --- ...", "SOS"),
        ('-.. . .- -.. .-.. .. -. .', "DEADLINE"),
        ('.... . .-.. .-.. ---  .-- --- .-. .-.. -..', "HELLOWORLD")
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result
