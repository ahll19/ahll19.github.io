---
layout: post
title: '"When are my popcorn done?" - part 1'
author: "Anders Lauridsen"
categories: journal
tags: [signalprocessing, audio, python, popcorndetection]
image: posts/2023-11-18/placeholder1.jpg
---

My hope is that one day this blog will be filled with overengineered solutions to problems that either don't exist, or are or of so little concern that they aren't worth the effort of solving.

One such non-problem is knowing when microwave popcorn are done popping. I had the idea when I had some friends over for a visit, and we wanted popcorn. I didn't want to leave the conversation, but I didn't want to leave the conversation. And while waiting for the popcorn to pop I started to wonder how one might automate the process of determining the doneness of microwave popcorn. My thought process was that since instructions on popcorn boxes often tell you to check the time between pops, if I could detect the individual pops, the challenge of determining doneness would be trivial. 

The code I wrote for this blog post, and the current state of the project, can be found at [This GitHub Repo](https://github.com/ahll19/popcorn_detection)

---

**Table of Contents**
---
- [1. Exploration](#1-exploration)
- [2. My Naive Algorithm](#2-my-naive-algorithm)
  - [2.1 Does the algorithm detect popcorn?](#21-does-the-algorithm-detect-popcorn)

---

# 1. Exploration
In order to test how I could detect individual pops, I needed to collect some data. This was done through a highly scientific process:

<center>Make microwave popcorn while recording it one my phone.</center>

After collecting data I loaded the resulting mp3 file into Python, in order to get a sense of what the data might look like.

My phone seems to have recorded at $32,000Hz$, which allows us plenty of resolution in frequency to analyze the popping of popcorn. In the figures below we see the waveform that the phone recorded, and the spectrogram of that waveform.

![Waveform of the popcorn popping](../assets/img/posts/2023-11-18/full_waveform.png)

![Spectrogram of the popcorn popping](../assets/img/posts/2023-11-18/full_spectgram.png)

Looking at the waveform we see quite a lot of noise from the microwave, which seems to be on the low end of the frequency spectrum, when looking at the spectrogram. We also see a big loss in energy at the top of the frequency range of the spectrogram, which I honestly can't explain, other than my phone might not be able to pick up such high frequencies. From the spectrogram it looks as though the popcorn might be visible as vertical lines on the spectrogram, meaning the individual pops are quite broad spectrum. So in designing the algorithm which is going to detect pops we assume two things for now:
1. The pops are more or less uniform in the frequency range of $2000Hz$ to $10,000Hz$.
2. The energy of the noise produced by the microwave is mostly of frequencies lower than $4000Hz$. 

Using this let's create a band pass filter using `Scipy`, and set the critical frequencies to $f_{c1}=4000Hz$ and $f_{c2}=10,000Hz$. Filtering a signal according to a Butterworth band pass filter can easily be achieved by the following code.

```python
x, sr = audio2numpy.audio_from_file("popcorn.mp3")
x /= np.max(np.abs(x))  # Normalize the recorded waveform
t = np.arange(0, len(x)) / sr

a = signal.butter(5, [4000, 10000], btype="band", fs=sr, output="sos")
y = signal.sosfiltfilt(a, x)
```

After filtering we can see on the waveform in the figure below that most of the noise of the microwave has been removed.

![Filtered waveform of the popcorn popping](../assets/img/posts/2023-11-18/filtered_waveform.png)

And now that we have removed much of the noise, we can zoom in on one single pop, and see what shape a pop takes in time (since we already "know" they are pulses which are uniform in frequency). Looking at the next figure we see that an impulse that decays exponentially. What is mostly of interest for this first implementation of a popcorn detector is the decay time, which from the plot below seems to be about 0.1 seconds. The exponentially decaying nature of the absolute waveform might be of interest in a more robust algorithm.

![Absolute waveform of a single popcorn popping](../assets/img/posts/2023-11-18/singlepop.png)

# 2. My Naive Algorithm
While using the shape of the shape of the waveform of a popcorn popping might be good for detecting individual pops, it seemed like a lot of work, so I chose to go with a more naive algorithm for now. 

I chose to use the uniformity of the spectrum of a popcorn pop, and came up with the following algorithm:
1. Calculate the STFT $X$ of the signal $x$.
2. Iterate through the time slices of $X$
   1. Check the mean value $\mu$ of the frequencies of $X$ which are between $f_{c1}$ and $f_{c2}$
   2. Calculate 
   $$
   \lambda=\sum_{f_{c1}< \omega < f_{c2}} |\mu - X_\omega(t) |^2
   $$
    for all the given time iteration $t$
   3. If $\lambda$ is larger than some threshold $\lambda_0$ then we call that a pop, and we skip the next iterations, corresponding to 0.1 seconds (this value is gained from the approximate time it takes a popcorn kernel to pop).
3. Calculate the time between each pop, and see if we are getting close to the value the manufacture specifies is the correct time between pops.

While this algorithm might seem ingenious and perfect, it does have some flaws that one might point out, even before testing it at all:
1. You have to know what value to set for $\lambda_0$.
2. The tool has no way of distinguishing between popcorn pops and perfect silence.
3. It might be slightly ineffective to carry out this many sums of squares calculations each second.
4. The algorithm doesn't allow for multiple pops to occur within a time-span of 0.1 seconds.

Do note that a plus of this algorithm is that we do not need to filter the signal, since we only consider the frequency range where we have assumed that no microwave noise is negligible. 

Hence, the title of this section. But no matter, let's see how this algorithm performs after tweaking the $\lambda_0$ parameter.

## 2.1 Does the algorithm detect popcorn?
By seeing what values $\lambda$ had for times when no popcorn were popping it seemed that $\lambda_0=4\cdot10^{-5}$ was a good value. This would remove most of the false positives induced by the noise in the signal, while still allowing relatively silent pops to be caught by the algorithm. I also cut the first 62 seconds of the signal for this test, since this is when the popcorn started popping.

Looking at the figure below, we see a wide angle view of when the individual pops where detected. By looking at the amount of red dots centered around the more busy parts of the signals, this seems to be a decent algorithm. 

![Wide view of popcorn detections](../assets/img/posts/2023-11-18/detected_popcorn_wide_test_1.png)

It is however not easy to make out individual pops this way, so I zoomed in on a part of the signal which highlights that this algorithm seems to work fine under the conditions of this test.

![Narrow view of popcorn detections](../assets/img/posts/2023-11-18/detected_popcorn_narrow_test_1.png)

Looking at the figure above we see that the algorithm actually gets decent performance on this part of the signal. Scanning across the waveform it looks like the algorithm catches most of the pops which occur. And looking at the resulting time between pops, it does look promising.

![Time between pops, not smoothed](../assets/img/posts/2023-11-18/time_between_pops_test_1.png)
![Time between pops, smoothed](../assets/img/posts/2023-11-18/time_between_pops_smoothed_test_1.png)

Seeing that taking a moving average with a window-size of 5 creates results that look like the one above, one might be tempted to slap this algorithm onto an Arduino Uno and wire it up to a microwave, and create a Kickstarter with a silly name. But this is a blog of science, so I did actually do more than one test on this algorithm.