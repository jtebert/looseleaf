# Looseleaf

## About

Looseleaf lets you keep a collaborative, organizable notebook of text, code snippets, and LaTeX math for teams and group projects. It was started at Hackbeanpot 2017. As students ourselves, we hope that this will be useful to others in our situation.

We started this at a hackathon and haven't fixed it from that yet. It's a cool concept, but not ready for real use yet. Content you add is currently viewable to the admins through the admin interface, so we **do not** recommend using it for any information you are remotely concerned about the privacy of. Also, the horrifying number of bugs means that you probably wouldn't like using this for anything yet, anyway. I'd classify it as very pre-alpha at this point.

## Current Features
- Create private notebooks
- Add notes to notebooks that are arrangeable, draggable, and resizable
- Notes support Markdown text, LaTeX math, and code snippets

## Known Issues and Missing Features (there are many)
- Adding collaborators when creating a notebook doesn't actually add them to the notebook
- All users are publically listed in the collaborators section when creating a new notebook
- No way to add or remove collaborators after a notebook is created
- List of collaborators for a notebook isn't shown anywhere
- The notebook color isn't used anywhere
- No way to delete notes or notebooks after they are created.
- Once a note is created, it can't be edited (the "Save" button on the edit form currently does nothing)
- Note editing form doesn't expand to show all text of the note
- No way to retrieve lost login information (need to set up emails through django-userena)
- There is plenty to be left desired on most of the user interface
- No syntax highlighting, fenced code blocks, or other extras in Markdown.
- If notes are deleted or edited by another user, these changes are not visible to the other user without a page refresh. This will cause many problems if users are editing a notebook simultaneously. Replacing ajax with websockets should solve this issues but will require a major overhaul of the django backend.
- Create some sort of contact and about pages on the website

## License

This project is licensed under the [MIT License](license.txt). If you would like to use or help develop it, please consider joining us in working on this project.
