# Workout\_Tracker

# To test:

```
# from top-most Workout_Tracker directory
$ export FLASK_APP=Workout_Tracker
$ export FLASK_ENV=development
$ pip3 install -e .
$ flask run

```

# TODO

* Understand how `redirect(url_for(<whatever>))` is different from
`render_template(<whatever>)` and how that affects the HTTP request type
(if at all)

* Add weight column to "Create Periodization Strategy" and make it so one of the
four options (weight, sets, reps, RPE/RIR) should remain open (the one that will
be open for each workout)

# Musings/Development Notes

* Noticing the benefit Agile would bring to the development process;
seeing as "software is never finished, only abandoned," (original quote by
Leonardo Da Vinci - "Art is never finished, only abandonded"), a perfectionist
will always have "just one more" thing to add before release. Recognizing that
you will never be able to forsee how a project will change, what will need to be
refactored, etc, will enforce good programming habits such as orthogonality. That
said, one shouldn't thoughtlessly rush to release; the push-pull between "just
get it out there" and "let's think about how this might change" should be
"Perfectly balanced, as all things should be." -Thanos

