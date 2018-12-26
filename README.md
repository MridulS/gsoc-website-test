# Projects

A website that showcases sub organizations! 

This website is based on the [ideas list](https://projects.coala.io) for GSoC by
the coala community.


## Purpose

This is designed for GSoC but can be used for other initiatives at the same
time. We use it for research theses, GSoC, GCI and maybe others in the future.

Why?

- It's way more appealing to students.
- You can search and filter sub organizations.
- Sub organizations as structured data are more concise and you're sure to have all
  points covered - at the same time we can show students an overview and showing
  the full information only when needed.

## Usage

To clone the repository and run this website on your local machine, [install Jekyll](https://jekyllrb.com/docs/installation/) for your OS and type the following commands:

    $ sudo gem install jekyll bundler
    $ git clone https://github.com/...
    $ cd projects
    $ bundle install
    $ bundle exec jekyll serve


Then you can simply go to either of the following addresses in your browser to access the site:

    127.0.0.1:4000
    localhost:4000

If you face problems while installing Jekyll or using its gem bundler you may go through its [troubleshooting docs](https://jekyllrb.com/docs/troubleshooting/)


## Defining FAQs

Users can also add FAQs by simply creating a markdown file in _faq folder.

Format for faq markdown file is as follows:
```
---
Question: <Write the question here>
---

Answer
```

<!-- ## Multi Language Support -->

<!-- NumFOCUS supports multiple 'human languages'. To add a translation of a project -->
<!-- in a language, the following steps can be followed: -->

<!-- - Create a folder with language code in ```data/locale``` folder. -->
<!-- - Create ```faq.json```, ```projects.json```, ```faq``` and ```projects``` folder -->
<!-- if they do not exist already. -->
<!-- - Add translated content of a project inside ```projects``` folder. The names of the -->
<!-- file should be same. -->
<!-- - Similiarly translated content of a faq goes inside ```data/locale/ < language-id > /faq``` -->
<!-- folder. -->
<!-- - For the faq.json and projects.json metadata, refer to Bahasa and Hindi -->
<!-- Translations available in ```data/locale``` directory. -->
<!-- - Lastly, in ```resources/js/app.js``` file, Add the new language json in Language service. -->
