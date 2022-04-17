[issue]: https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/issues/39
[repo]: https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin

# mkdocs-pagenav-generator
This MkDocs-plugin was born after [I made an issue on the awesome-pages repository][issue] asking if it was possible to replace a specific text within a md-file with whatever pages are in the same directory.  
The maintainer responded with a code-example and since they don't have time to manage another project did I quickly make this repo, so that people can install and use it.

## Setup
In order to use this plugin will you need to install it using pip:

```
pip install git+https://github.com/Andre601/mkdocs-pagenav-generator
```

This plugin requires the awesome-pages plugin to be installed too. So make sure to have it installed using pip:

```
pip install mkdocs-awesome-pages-plugin
```

After you've finished the installation will you need to add it as a plugin to your `mkdocs.yml`

```yaml
plugins:
  - awesome-pages # Required
  - pagenav-generator
```

## Usage
In our example do we have the following folder structure:

```yaml
docs/
 ├ index.md
 ├ assets/
 │  └ images/ # Just some images
 │     └ cat.jpeg # Cute cats :3
 └ posts/
    ├ .pages.yml # Page navigation of awesome-pages
    ├ index.md   # This is the page with the {nav} placeholder
    ├ post1.md
    ├ post2.md
    └ archive/
       └ post3.md
```

It is important, that you have a `.pages.yml` file in the directory, where you want to use the placeholder in, so that the plugin can retrieve the file structure through it.  
In our case does the `docs/posts/.pages.yml` file have the following structure:  

```yaml
nav:
- 'My Posts': index.md
- ... # List all pages and their subdirectories
```

The next step is to add the `{nav}` placeholder.  
This placeholder would be replaced with the list of pages matching those configured in your `.pages.yml` file.

```markdown
# My Posts
This page lists all my posts I made.  
Take a look at the nav list below.

## Posts
{nav} <!-- This will be replaced by the plugin -->
```

With the aforementioned folder structure would the placeholder now be replaced with the following structure:

```html
<ul>
  <li><a href="post1/">Post1</a></li>
  <li><a href="post2/">Post2</a></li>
  <li>Archive
    <ul>
      <li><a href="archive/post3/">Post3</a></li>
    </ul>
  </li>
</ul>
```

## Notes
This plugin was **not** created by me. I do **not** claim to have copyright or ownership in any way for this plugin.  
This plugin was created by lukasgeiter and is shared with his permission.

Since I know absolutely nothing about Python do I not maintain nor update this plugin. The software is provided "as is" without warranty or liability.
Do not contact me or lukasgeiter for help with this plugin.
