# Hephaestus

** As of Dec 2025, this project is no maintained, nor available for installation through PyPi.**

I made this decision for a few reasons:
    1. Much of the code here isn't useful in the real world and contains many anti-patterns.
    2. I wanted to free up the name hephaestus-lib for future use.
    3. There's too much generality here. 
        - Python library I make in the future (if any) will be much smaller and focused.
    4. It'll be much easier to restart and salvage the good, rather than refactor. 


## Table of Contents
1. [Objective](#objective)
2. [Use](#use)
    - [Installation](#installation)
    - [Testing](#testing)
    - [Generating Documentation](#generating-documentation)
3. [Inspirations](#inspirations)
4. [Future Plans](#future-plans)
    - [Short Term Goals](#short-term-goals)
    - [Long Term Goals](#long-term-goals)


## Objective

The objective of this project was/is to stop repeating myself. I've gotten tired of rewriting the same modules and utilities
for various professional and hobby project.

Started in December 2024, well... technically, since about 2022.

## Use

While not intentionally developed to be cross-platform, most of the stuff in here is. It just didn't cost that that much more effort 
or brainpower to avoid.

This library is not intended to be used as a template or guide, but it can definitely can be used as "inspiration." Please link back to this repo or [MalakaiSpann.com](https://malakaispann.com) if you do.


### Testing

```bash
scripts/run_pytest
```

### Generating Documentation
```bash
scripts/generate_documentation
```

Friendly reminder: don't be a weirdo who steals source code. Even when credited, it's still pretty shady to straight copy someone else's work. The occasional peak when you're stuck is fine, but learn how to do it yourself... it'll get you much farther!

## Future Plans

This is likely going to be a Work-In-Progress for quite some time. There's lots to do even with the small amounts of 
code already in here.

I plan on updating/improving this library as long as I use Python 🙂.  

### Short Term Goals
- Get sane CI pipeline together.
    - A lot of the scripts are already there, just kinda need to set everything up to talk to one another.
- Finish documentation. Get it together man.
- Implement code coverage reporting. This is always a good step
- Knock out some unit and functional tests. Many of the things in here are 

### Long Term Goals
- World Peace
- Afford a house
- Live in Japan

Feel free to suggest improvements or get down and dirty (with protection of course... a merge request – I mean a merge request).

Thanks, 

\- Kay
