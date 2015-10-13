import mock

from b import toast


@mock.patch('a.Toaster.burn')
@mock.patch('b.burn')
def test_toast(mock_burn, mock_t_burn):
    assert toast() is True
    mock_burn.assert_called_once_with()
    mock_t_burn.assert_called_once_with()


if __name__ == "__main__":
    test_toast()
