---
layout: page
title: About
---

<style>
.floated_img
{
    float: left;
}
</style>

<p class="message">
  <strong>Currently:</strong>  PhD Student at Virginia Tech (VT) in
  <a href="http://gbcb.vbi.vt.edu/">Genetics, Bioinformatics, and Computational Biology</a> (GBCB).

  <br>
  Volunteer instructor for
  <a href="https://carpentries.org/">The Carpentries</a>
  (<a href="http://software-carpentry.org/">Software Carpentry</a> and
  <a href="http://www.datacarpentry.org/">Data Carpentry</a>)
  <br>
  <br>
  <a href="https://www.archlinux.org/">Arch</a>
  <a href="https://antergos.com/">Linux</a> user (thanks to my co-worker,
  <a href="http://dads2busy.github.io/">Aaron Schroeder</a>)
  and (co)maintain the
  <a href="https://aur.archlinux.org/packages/rstudio-desktop-preview-bin/">rstudio-desktop-preview-bin</a>,
  <a href="https://aur.archlinux.org/packages/nteract-bin/">nteract</a>,
  and
  <a href="https://aur.archlinux.org/packages/rodeo/">rodeo</a>
  packages in the
  <a href="https://aur.archlinux.org/">AUR</a>.
  <br>
  <br>
  Data Scientist at
  <a href="http://www.landeranalytics.com/">Lander Analytics</a>
  with
  <a href="http://www.jaredlander.com/">Jared Lander</a>
  <br>
  <br>
  <strong>Past:</strong>
  <a href="https://www.mailman.columbia.edu/become-student/degrees/masters-programs/masters-public-health/columbia-mph">Masters of Public Health</a> in
  <a href="https://www.mailman.columbia.edu/become-student/departments/epidemiology">Epidemiology</a>
  from
  <a href="https://www.mailman.columbia.edu/">Columbia University Mailman School of Public Health</a>.
  Bachelors of Arts in
  <a href="http://www.hunter.cuny.edu/psychology">Psychology</a>
  where I studied
  <a href="http://catalog.hunter.cuny.edu/preview_program.php?catoid=6&poid=793">Behavioral Neuroscience</a>
  and minors in
  <a href="http://www.hunter.cuny.edu/csci/for-students/minoring-in-computer-science">Computer Science</a>
  and
  <a href="http://catalog.hunter.cuny.edu/preview_program.php?catoid=16&poid=2270&returnto=1728">Biology</a>
  from
  <a href="http://www.macaulay.cuny.edu/">The Macaulay Honors College</a>
  at <a href="https://www.google.com/search?q=cuny+hunter+college&oq=cuny+hunter+college&aqs=chrome.0.0j69i65l2j0l3.2012j0j1&sourceid=chrome&ie=UTF-8">Hunter College</a> of
  <a href="http://www2.cuny.edu/">The City University of New York</a>.
  <br>
  <a href="http://stuy.enschool.org/">Stuyvesant High School</a> alumnus.
  <br>
  <br>
  CV
</p>

<h1>Podcasts</h1>


{% for podcast in site.podcasts %}
  <div class="floated_img">
    <a href="{{ podcast.url }}">
      <img src="{{ podcast.image }}"
      title="{{ podcast.name }}"
      style="width:{{ site.podcast_settings.global_size_width }};
             height:{{ site.podcast_settings.global_size_height }};">
    </a>
  </div>
{% endfor %}
