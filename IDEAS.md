# Project Ideas & Tasks

This file contains a list of ideas, features, and tasks to be implemented for the Design System website clone project.

## Idea #1: Create the Services Page

- **Status:** `[ ] To Do`
- **Description:** The main navigation in `index.html` links to `services.html`, but this page doesn't exist yet. Create the `services.html` page using the content from `ds-services.md`.
- **Acceptance Criteria:**
  - A new `services.html` file should be created.
  - It should have a structure similar to `index.html` (header, main content, footer).
  - The content should be parsed and styled from `ds-services.md`.
  - The styles for the services page that are already in `style.css` (like `.service-section`) should be used.

## Idea #2: Enhance Project Card Video Interaction

- **Status:** `[ ] To Do`
- **Description:** Currently, the videos on the project cards in `index.html` are static. It would be more engaging if the videos played on mouse hover and paused when the mouse leaves.
- **Acceptance Criteria:**
  - Add JavaScript to `index.html`.
  - When a user hovers over a `.project-card`, the video inside it should start playing.
  - When the user's mouse leaves the card, the video should pause and reset to the beginning.

## Idea #3: Implement Mobile Navigation

- **Status:** `[ ] To Do`
- **Description:** The CSS in `style.css` hides the navigation links on mobile (`.nav-links { display: none; }`). A proper mobile menu (e.g., a "hamburger" menu) needs to be implemented.
- **Acceptance Criteria:**
  - Add a hamburger menu icon for screen sizes below 768px.
  - When the icon is clicked, the navigation links should appear in a mobile-friendly overlay or dropdown.
  - This will require changes to `index.html`, `style.css`, and the JavaScript block.

## Idea #4: Create a Contact Page with WhatsApp Integration

- **Status:** `[ ] To Do`
- **Description:** Create a new `contact.html` page that provides users with multiple ways to get in touch. The page should feature a modern panel for initiating a WhatsApp chat and a standard, simple contact form.
- **Acceptance Criteria:**
  - A new `contact.html` file is created and linked in the site's navigation and footer.
  - A visually appealing panel mimicking WhatsApp's branding is implemented.
  - The WhatsApp panel contains a button that, when clicked, opens the WhatsApp application to a pre-defined number.
  - A simple contact form is present on the page, containing a "Name" field, a "Content" textarea, and a "Send Message" button.
  - The page's styling is consistent with the overall design of the website.