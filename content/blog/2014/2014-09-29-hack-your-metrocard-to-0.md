---
layout: post
title:  "Hacking Your MetroCard to $0.00"
date:   2014-09-29 20:40:00

#categories: lifehack mta metrocard

tags:
  - lifehack
  - mta
  - metrocard
---

Earlier this month, Ben Wellington wrote a blog post about
[How Memorizing “$19.05” Can Help You Outsmart the MTA](http://iquantny.tumblr.com/post/96700509489/how-memorizing-19-05-can-help-you-outsmart-the-mta).
A few days later, after the post went viral, the MTA
[responded](http://iquantny.tumblr.com/post/97027810529/update-mta-cites-lack-of-infinite-change-in-current)
by saying this is so there will be enough change in the machine for cash
users and this will be addressed next year after the new fare increase.

<!-- more -->

Ben suggested to us all to remember `$9.55`, `$19.05`, and `$38.10` to get a
MetroCard that will yield us a `$0.00` card at the end.  Among all the
comments I saw going around my social media feeds, one of the comments
that I saw was how remembering these magic numbers are great, but people
are still annoyed that there will always be a few cents left over
depending on when you read about the magic fares.

If we look closer at the table Ben shared (partially reproduced
below), and take in to account the fact that the kiosks will only
take in whole nickel values (i.e., values that end in either `5` or `0`),
we can see one thing...

| # Rides | You Pay ($) | On Card ($) | Remainder ($) |
|---------|-------------|-------------|---------------|
| 1       | 2.40        | 2.52        | 0.02          |
| 2       | 4.80        | 5.04        | 0.04          |
| 3       | 7.15        | 7.51        | 0.01          |
| 4       | 9.55        | 10.03       | 0.03          |
| 5       | 11.90       | 12.50       | 0.00          |
| 8       | 19.05       | 20.00       | 0.00          |
| 13      | 30.95       | 32.50       | 0.00          |

... there are ways for us to generate `$0.01`, `$0.02`, `$0.03`, and `$0.04`
remainders in our card!  What does that mean for us?  It means
regardless of how many leftover cents your card will have, there is
always a way to get it up to a whole nickel value.  From there we can
input one of the three magical values plus the amount needed to get
you to a whole nickel value + how much you are currently short.

Let's walk through an example.

You buy a 'Fast $9 MetroCard', You end up with `$9.45` on it.  By the
time you've used it to exhaustion, you will have `$1.95` on it.  You are
'short' `$2.50 - $1.95 = $0.55`.  So you go to the kiosk and put in
`$19.05 + $0.55 = $19.60`, and voilà.  You now have an 9 ride
MetroCard.

Let's say you have a MetroCard laying around with `$0.01` on it.  We
know we need `$0.04` to get a whole nickel value.  We can look up on
the table some value that gives us `$0.04`, so we add `$4.80` on the
card.  This gives us a `$5.05` MetroCard.  Nice! we have a whole
nickel amount.  If we use this card to exhaustion, we will end with
`$0.05`, leaving us short `$2.45` for the next full ride.  We can now
use one of the 3 magical numbers in conjunction with the `$2.45` to
get us a MetroCard bound for `$0.00`.

If you wanted to do this all in one go... is we added `$4.80 + $2.45 +
$19.05 = $26.30` to to our card.

I haven't accounted for any weird 5% bonuses the kiosks may/may not
give you.  But the premise is simple, use one of the pre-calculated
values to 'nickel-out' your card, then use one of the magic values +
difference and you'll have one fewer thing to be worried about.
