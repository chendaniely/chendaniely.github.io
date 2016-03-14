---
layout: page
title: Research
permalink: /research/
---

Integrating hospital data in order to perform predictive health
analytics and building clinical support tools for clinicians through
meaningful use.  Currently interested in:

1.  inter- and intra- hospital networks and comparing care
coordination networks to improve patient outcomes and
1.  improving communication and patient care between multidisciplinary
care coordination teams.

Disease-specific, unplanned hospital readmission within 30 days of
discharge are publically reported and risk-adjustment methods lack
ways of properly distinguishing difficulty of delivering care.

Increasingly, the needs of patients with complex medical
conditions cannot be met by a single healthcare provider.  To avoid
fragmentation of medical care among multiple consultants and services,
hospital-based responses have been to manage complex, comorbid
patients with Multidisciplinary Disease Teams (MDT). The key task of
the MDT teams during a MDT meeting, often under the leadership of a
specialist, is to collate and review information about the patient and
their disease, discuss it, and make a decision for further
investigation and treatment.

 <h1 class="page-heading">Research Related Posts</h1>

   <ul class="post-list">
	 {% for post in site.categories.Research %}
	   <li>
		 <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

		 <h2>
		   <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
		 </h2>
	   </li>
	 {% endfor %}
   </ul>

<!--
1. network stuff
1. network implications
1. describe an example -- what is this a co-morbid MDT
   1. imagine the following:
	  1. i said to him, he said to me, and she said to someone else, and someone dies
1. where has network science
   1. maybe network science made some progress, amd were can I develop
   1. where is the best place to apply network science
   1. what is known about these teams and forgetting networks,
   1. and what are the gaps in knowledge
   1. high citation counts in good journals
-->
