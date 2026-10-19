"""Unit and integration tests for the React Native mobile sandbox runner and curriculum."""

import pytest
from bot.codelab.react_native_sandbox import run_student_react_native_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_rn import RN_TUTOR_CHAPTERS


def test_rn_raw_elements():
    code = "<View><Text>Hello Mobile App!</Text></View>"
    res = run_student_react_native_code(code)
    assert res.success is True
    assert "<View><Text>Hello Mobile App!</Text></View>" in res.output


def test_rn_home_screen_component():
    code = """
    function HomeScreen() {
        return (
            <View>
                <Text>Welcome to CodeBuddy Mobile!</Text>
            </View>
        );
    }
    """
    res = run_student_react_native_code(code)
    assert res.success is True
    assert "<View><Text>Welcome to CodeBuddy Mobile!</Text></View>" in res.output


def test_rn_styling():
    code = """
    <View style={{ backgroundColor: "#2563eb" }}>
        <Text style={{ color: "#ffffff" }}>Mobile App</Text>
    </View>
    """
    res = run_student_react_native_code(code)
    assert res.success is True
    assert "background-color:#2563eb" in res.output


def test_rn_touchable_opacity():
    code = """
    <TouchableOpacity style={{ backgroundColor: "#10b981" }}>
        <Text style={{ color: "#ffffff" }}>Tap Me</Text>
    </TouchableOpacity>
    """
    res = run_student_react_native_code(code)
    assert res.success is True
    assert "<TouchableOpacity" in res.output
    assert "Tap Me" in res.output


def test_rn_scrollview():
    code = """
    <ScrollView>
        <Text>Feed Item 1</Text>
        <Text>Feed Item 2</Text>
    </ScrollView>
    """
    res = run_student_react_native_code(code)
    assert res.success is True
    assert "<ScrollView><Text>Feed Item 1</Text><Text>Feed Item 2</Text></ScrollView>" in res.output


def test_rn_contact_card_props():
    code = """
    function ContactCard(props) {
        return (
            <View>
                <Text>{props.name}</Text>
                <Text>{props.phone}</Text>
            </View>
        );
    }
    """
    res = run_student_react_native_code(code)
    assert res.success is True
    assert "Sara" in res.output
    assert "+251 91 123 4567" in res.output


def test_rn_raw_text_in_view_error():
    # React Native strictly prohibits text directly inside View
    code = "<View>This text has no Text tag</View>"
    res = run_student_react_native_code(code)
    assert res.success is False
    assert "Mobile Constraint" in res.friendly_explanation_en
    assert "የሞባይል ህግ" in res.friendly_explanation_am


def test_rn_html_tags_rejection():
    # React Native does not support HTML tags
    code = "<div><p>Hello HTML</p></div>"
    res = run_student_react_native_code(code)
    assert res.success is False
    assert "No HTML on Mobile" in res.friendly_explanation_en
    assert "በሞባይል ላይ የ HTML ታጎች የሉም" in res.friendly_explanation_am


def test_rn_curriculum_chapters():
    chapters = get_all_tutor_chapters("react_native")
    assert len(chapters) == 7
    assert chapters[0].id == "rn_ch1"
    assert chapters[6].id == "rn_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("rn_ch1")
    assert ch1 is not None
    assert ch1.track == "react_native"

    next_id = get_next_tutor_chapter_id("rn_ch1")
    assert next_id == "rn_ch2"

    last_next = get_next_tutor_chapter_id("rn_ch7")
    assert last_next is None
