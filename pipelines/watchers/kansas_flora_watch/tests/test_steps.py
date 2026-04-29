from pipelines.watchers.kansas_flora_watch.steps import (
    acquire,
    bundle,
    detect,
    normalize,
    publish,
    validate_dwca,
)


def test_step_modules_append_name_in_order() -> None:
    context: dict = {}

    for module in (detect, acquire, validate_dwca, normalize, bundle, publish):
        context = module.run(context)

    assert context["steps"] == [
        "detect",
        "acquire",
        "validate_dwca",
        "normalize",
        "bundle",
        "publish",
    ]


def test_step_modules_reuse_existing_steps_list() -> None:
    context = {"steps": ["already_there"]}

    updated = detect.run(context)

    assert updated is context
    assert updated["steps"] == ["already_there", "detect"]
