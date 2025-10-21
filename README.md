# Project: Design System Agency Website Clone

This project is a simple clone of the Design System agency website, built with HTML and CSS. It includes a home page with a project grid, a style guide, and a README file with instructions on how to maintain and extend the website.

## Getting Started

To view the website, simply open the `index.html` file in your web browser. There are no special build steps or dependencies required.

## Project Structure

```
/
├── index.html              # The main home page
├── style.css               # Main stylesheet for the website
├── style-guide.html        # The style guide page
├── style-guide.css         # Stylesheet for the style guide page
├── README.md               # This file
└── ...                     # Other project files
```

## Style Guide

The project includes a style guide to ensure a consistent look and feel across the website. You can view the style guide by opening `style-guide.html` in your browser. The style guide documents the color palette, typography, and UI elements used in the project.

Please refer to the style guide before making any changes to the website's design.

## How to Add a New Project

To add a new project to the home page, you need to edit the `index.html` file. Follow these steps:

1.  Open `index.html` in a text editor.
2.  Locate the `<div class="project-grid">` element.
3.  Inside the grid, you will find several `<article class="project-card">` elements. Copy one of these elements to create a new project.
4.  Update the content of the new project card:
    *   Change the `<h3>` text to the project title.
    *   Change the `<p>` text to the project description.
    *   Update the `<source>` tag within the `<video>` element to point to the new project's video file.

Here is an example of a project card:

```html
<article class="project-card">
    <a href="#">
        <div class="card-media">
            <video loop muted playsinline preload="metadata">
                <source src="[URL_TO_YOUR_VIDEO]" type="video/mp4">
            </video>
        </div>
        <div class="card-content">
            <h3>New Project</h3>
            <p>A brief description of your new project.</p>
        </div>
    </a>
</article>
```

## Deployment

This is a static website, so you can deploy it to any static web hosting service, such as GitHub Pages, Netlify, or Vercel. Simply upload the files to your hosting provider.