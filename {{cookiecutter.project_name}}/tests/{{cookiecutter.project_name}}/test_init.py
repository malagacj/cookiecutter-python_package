"""Sample test module for __init__ file"""

from myproject import main


def test_main(capsys) -> None:
    """Sample test for main function"""
    main()
    captured = capsys.readouterr()  # Capture the output
    assert captured.out == "Hello from myproject!\n"
