from qrcode_generator.defaults import DefaultsFileManagent as dfm
from qrcode_generator.parser import QRCode_Parser
from qrcode_generator.qr import _fallback_title_from_url, _parse_batch_lines


def test_parse_batch_lines_ignores_comments_and_blank_lines() -> None:
    lines = [
        "\n",
        "# comment\n",
        "https://example.com\n",
        "https://openclaw.ai (OpenClaw)\n",
    ]

    assert _parse_batch_lines(lines) == [
        ("https://example.com", None),
        ("https://openclaw.ai", "OpenClaw"),
    ]


def test_fallback_title_from_url_uses_hostname() -> None:
    assert _fallback_title_from_url("https://example.com/some/path") == "example.com"


def test_fallback_title_from_url_sanitizes_non_alnum() -> None:
    assert _fallback_title_from_url("hello world/?x=1") == "hello_world"


def test_parser_builds_qrcode_from_args() -> None:
    parser = QRCode_Parser(
        [
            "--url",
            "https://example.com",
            "--title",
            "Example",
            "--output-dir",
            "./tmp-output",
        ]
    )

    assert parser.args.url == "https://example.com"
    assert parser.args.title == "Example"
    assert parser.args.output_dir == "./tmp-output"
    assert parser.qr_code.file_prefix == dfm.FILE_PREFIX
    assert parser.qr_code.print_title is True


def test_parser_no_title_flag_disables_title_rendering() -> None:
    parser = QRCode_Parser(["--url", "https://example.com", "--no-title"])

    assert parser.qr_code.print_title is False
