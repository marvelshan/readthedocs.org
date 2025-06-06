Contributing to Read the Docs
=============================

Are you here to help on Read the Docs? Awesome! |:heart:|

Read the Docs, and all of it's related projects, are all community maintained,
open-source projects. We hope you feel welcome as you begin contributing to any
of these projects. You'll find that development is primarily supported by our
core team members, who all work on Read the Docs full-time.

All members of our community are expected to follow our :doc:`/code-of-conduct`.
Please make sure you are welcoming and friendly in all of our spaces.

Get in touch
------------

If you have a question or comment, we generally suggest the following
communication channels:

- Ask usage questions ("How do I?") on `StackOverflow`_.
- Report bugs, suggest features, or view the source code `on GitHub`_.

.. _StackOverFlow: https://stackoverflow.com/questions/tagged/read-the-docs
.. _on GitHub: https://github.com/readthedocs/readthedocs.org

Contributing
------------

There are plenty of places to contribute to Read the Docs, but if you are just
starting with contributions, we suggest focusing on the following areas:

.. contents::
    :local:

.. tip::
    You can also contribute to the `Read the Docs Sphinx Theme`_,
    or Sphinx extensions in the `Read the Docs GitHub organization`_ like `sphinx-notfound-page`_.

.. _Read the Docs Sphinx Theme: https://sphinx-rtd-theme.readthedocs.io/en/stable/
.. _Read the Docs GitHub organization: https://github.com/readthedocs
.. _sphinx-notfound-page: https://github.com/readthedocs/sphinx-notfound-page

Contributing to development
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to deep dive and help out with development on Read the Docs, then
first get the project installed locally according to the
:doc:`installation guide </install>`. After that is done we
suggest you have a look at tickets in our issue tracker that are labelled `Good
First Issue`_. These are meant to be a great way to get a smooth start and
won't put you in front of the most complex parts of the system.

If you are up to more challenging tasks with a bigger scope,
then there are a set of tickets with a `Feature`_ or `Improvement`_ tag.
These tickets have a general overview and description of the work required to finish.
If you want to start somewhere, this would be a good place to start
(make sure that the issue also have the `Accepted`_ label).
That said, these aren't necessarily the easiest tickets.
They are simply things that are explained.
If you still didn't find something to work on, search for the `Sprintable`_ label.
Those tickets are meant to be standalone and can be worked on ad-hoc.

You can read all of our :doc:`/index` to understand more the development of Read the Docs.
When contributing code, then please follow the standard Contribution Guidelines set forth at `contribution-guide.org`_.

.. _Feature: https://github.com/readthedocs/readthedocs.org/issues?direction=desc&labels=Feature&page=1&sort=updated&state=open
.. _Improvement: https://github.com/readthedocs/readthedocs.org/issues?q=is%3Aopen+is%3Aissue+label%3AImprovement
.. _Accepted: https://github.com/readthedocs/readthedocs.org/issues?q=is%3Aopen+is%3Aissue+label%3AAccepted
.. _Good First Issue: https://github.com/readthedocs/readthedocs.org/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22
.. _Sprintable: https://github.com/readthedocs/readthedocs.org/issues?q=is%3Aopen+is%3Aissue+label%3ASprintable
.. _contribution-guide.org: http://www.contribution-guide.org/#submitting-bugs


Contributing to documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation for Read the Docs itself is hosted by Read the Docs at https://docs.readthedocs.io (likely the website you are currently reading).

There are guidelines around writing and formatting documentation for the project.
For full details, including how to build it, see :doc:`/docs`.

Contributing to translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We use Transifex to manage localization for all of our projects that we support
localization on. If you are interested in contributing, we suggest joining a
team on one of `our projects on Transifex`_. From there, you can suggest
translations, and can even be added as a reviewer, so you can correct and
approve suggestions.

If you don't see your language in our list of approved languages for any of our
projects, feel free to suggest the language on Transifex to start the process.

.. _our projects on Transifex: https://explore.transifex.com/readthedocs/

Triaging issues
---------------

Everyone is encouraged to help improving, refining, verifying and prioritizing
issues on Github. The Read the Docs core :external+rtd:doc:`team` uses the following
guidelines for issue triage on all of our projects. These guidelines describe
the issue lifecycle step-by-step.

.. note:: You will need Triage permission on the project in order to do this.
          You can ask one of the members of the :external+rtd:doc:`team` to give you access.

.. tip:: Triaging helps identify problems and solutions and ultimately what
         issues that are ready to be worked on. The core
         :external+rtd:doc:`team` maintains a separate :doc:`/roadmap`
         of prioritized issues - issues will only end up on that Roadmap after
         they have been triaged.

Initial triage
~~~~~~~~~~~~~~

When sitting down to do some triaging work, we start with the `list of
untriaged tickets`_. We consider all tickets that do not have a label as
untriaged. The first step is to categorize the ticket into one of the
following categories and either close the ticket or assign an appropriate
label. The reported issue …

… is not valid
    If you think the ticket is invalid comment why you think it is invalid,
    then close the ticket. Tickets might be invalid if they were already fixed
    in the past or it was decided that the proposed feature will not be
    implemented because it does not conform with the overall goal of Read the
    Docs. Also if you happen to know that the problem was already reported,
    reference the other ticket that is already addressing the problem and close the duplicate.

    Examples:

    - *Builds fail when using matplotlib*:
      If the described issue was already fixed, then explain and instruct to
      re-trigger the build.
    - *Provide way to upload arbitrary HTML files*:
      It was already decided that Read the Docs is not a dull hosting platform
      for HTML. So explain this and close the ticket.

.. _triage-not-enough-information:

… does not provide enough information
    Add the label **Needed: more information** if the reported issue does not
    contain enough information to decide if it is valid or not and ask on the
    ticket for the required information to go forward. We will re-triage all
    tickets that have the label **Needed: more information** assigned. If the
    original reporter left new information we can try to re-categorize the
    ticket. If the reporter did not come back to provide more required
    information after a long enough time, we will close the ticket (this will be
    roughly about two weeks).

    Examples:

    - *My builds stopped working. Please help!*
      Ask for a link to the build log and for which project is affected.

… is a valid feature proposal
    If the ticket contains a feature that aligns with the goals
    of Read the Docs, then add the label **Feature**. If the proposal
    seems valid but requires further discussion between core contributors
    because there might be different possibilities on how to implement the
    feature, then also add the label **Needed: design decision**.

    Examples:

    - *Provide better integration with service XYZ*
    - *Achieve world domination* (also needs the label **Needed: design
      decision**)

… is a small change to the source code
    If the ticket is about code cleanup or small changes to existing features
    would likely have the **Improvement** label.
    The distinction for this label is that these issues have a lower priority than a Bug,
    and aren't implementing new features.

    Examples:

    - *Refactor namedtuples to dataclasess*
    - *Change font size for the project's title*

… is a valid problem within the code base:
    If it's a valid bug, then add the label **Bug**. Try to reference related
    issues if you come across any.

    Examples:

    - *Builds fail if conf.py contains non-ascii letters*

… is a currently valid problem with the infrastructure:
    Users might report about web server downtimes or that builds are not
    triggered. If the ticket needs investigation on the servers, then add the
    label **Operations**.

    Examples:

    - *Builds are not starting*

.. _triage-support-tickets:

… is a question and needs answering:
    If the ticket contains a question about the Read the Docs platform or the
    code, then add the label **Support**.

    Examples:

    - *My account was set inactive. Why?*
    - *How to use C modules with Sphinx autodoc?*
    - *Why are my builds failing?*

… requires a one-time action on the server:
    Tasks that require a one time action on the server should be assigned the
    two labels **Support** and **Operations**.

    Examples:

    - *Please change my username*
    - *Please set me as owner of this abandoned project*

After we finished the initial triaging of new tickets, no ticket should be left
without a label.

.. _list of untriaged tickets: https://github.com/readthedocs/readthedocs.org/issues?q=is:issue+is:open+no:label

Additional labels for categorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additionally to the labels already involved in the section above, we have a
few more at hand to further categorize issues.

*High Priority*
    If the issue is urgent, assign this label. In the best case also go forward to
    resolve the ticket yourself as soon as possible.

*Good First Issue*
    This label marks tickets that are easy to get started with. The ticket
    should be ideal for beginners to dive into the code base. Better is if the
    fix for the issue only involves touching one part of the code.

*Sprintable*
    Sprintable are all tickets that have the right amount of scope to be
    handled during a sprint. They are very focused and encapsulated.

For a full list of available labels and their meanings, see
:doc:`/issue-labels`.

Helpful links for triaging
~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a list of links for contributors that look for work:

- `Untriaged tickets
  <https://github.com/readthedocs/readthedocs.org/issues?q=is:issue+is:open+no:label>`_:
  Go and triage them!
- `Tickets labelled with Needed: more information
  <https://github.com/readthedocs/readthedocs.org/issues?utf8=✓&q=is:open+is:issue+label:"Needed:+more+information">`_:
  Come back to these tickets once in a while and close those that did not get
  any new information from the reporter. If new information is available, go
  and re-triage the ticket.
- `Tickets labelled with Operations
  <https://github.com/readthedocs/readthedocs.org/issues?q=is:open+is:issue+label:Operations>`_:
  These tickets are for contributors who have access to the servers.
- `Tickets labelled with Support
  <https://github.com/readthedocs/readthedocs.org/issues?q=is:open+is:issue+label:Support>`_:
  Experienced contributors or community members with a broad knowledge about
  the project should handle those.
- `Tickets labelled with Needed: design decision
  <https://github.com/readthedocs/readthedocs.org/issues?q=is:open+is:issue+label:"Needed:+design+decision">`_:
  Project leaders must take actions on these tickets. Otherwise no other
  contributor can go forward on them.
