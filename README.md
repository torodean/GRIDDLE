# GRIDDLE

## About

The Git Repository Indexing and Digital Documentation Linking Engine (GRIDDLE) is a system designed to unify and streamline documentation across one more more Git repository.
It automatically aggregates, indexes, and interconnects documentation, enabling seamless navigation and discovery.
By detecting relationships between disparate documents and generating intelligent cross-links, GRIDDLE transforms fragmented repo-level docs into a cohesive, searchable documentation network.

## Background and Motivation

The goal of GRIDDLE is to help organize and maintain documentation in a way which is both easy to access and easy to find relavent documents.
The goal of improved and accessible documentation is a common one for many projects and exists on many levels and in many forms.
The GRIDDLE solution aims to be versatile, adaptable, and provide a common framework to implement in various environments.

Through one case study of a project hosted in Gitlab, the following issues (to name a few) were perceived.
Within the newer system of GitLab, there appears to be some issues with documentation being spread too far and wide without connection to the rest of the network.
In some cases, duplicate documents exist or are created because people are not aware of the documents that currently exist.
In other cases, documents may reference similar things but no linkage or commonality between the documents exist.
The largest issues that I have perceived are as follows:

- The documentation in GitLab is not easily searchable.
- Documentation continues to be lost and forgotten as the location or links to it dissappear.
- Duplicate documents exist because of the above two bullets.
- Documentation does not link to other relavent documents.

The purpose of GRIDDLE is to primarily solve the last bullet mentioned directly above ("documentation does not link to other relavent documents").
At the same time, it attempts to solve this problem in a way which also reduces the impact of the other bullet points mentioned.
By solving the linkage between documents, the documentation will ultimately be more easily accessible, findable, and available.

## Existing Implementation

This section will explain an already functional and existing system which was developed for a personal hobby project but forms the motivation and basic concepts behind GRIDDLE.
You can skip this section, but it will contain working examples of what GRIDDLE aims to produce as well as explanations of various challenges and other design considerations.
The original system exists within a project I created called MMORPDND (Massively Multiplayer Online Role-Playing Dungeons & Dragons). The primary feature of this project is that of organizing and storing notes for a dungeons and dragons world. These notes are setup in such a way where using simple text documents, I can automatically generate a fully interconnected set of documentation complete with automated hyperlinking to appropriate files, indexed pages with a browsable directory structure, and consistent formatting. The system uses Python to accomplish all of the various tasks.

- The full documentation for the MMORPDND project can be found [here](https://github.com/torodean/DnD/blob/main/docs/Manual.pdf).
  - Specifically, look at the `Tools And Scripts > mmorpdnd.py` section.
- The MMORPDND indexed directory structure with example pages complete with appropriate hyperlinking can be found [here](https://mmorpdnd.github.io/database/campaign/index.html).
