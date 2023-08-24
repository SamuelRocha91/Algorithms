import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 0)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("xablau", "tiririca")

    assert encrypt_message("xablau", 8) == "ualbax"

    assert encrypt_message("xablau", 3) == "bax_ual"

    assert encrypt_message("xablau", 4) == "ua_lbax"
