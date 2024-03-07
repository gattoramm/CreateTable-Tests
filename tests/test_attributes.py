import pytest


@pytest.mark.parametrize('dirname, expected', [
    ('dir1_fixture', 'expected1'),
    ('dir2_fixture', 'expected2')])
def test_directory_command(dirname, expected, request):
    result = my_package.directory_command(request.getfixturevalue(dirname))
    assert result == expected