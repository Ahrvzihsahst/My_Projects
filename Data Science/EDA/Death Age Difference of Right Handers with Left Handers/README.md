# Left-Handed People's Age at Death Analysis


### 1. Where are the old left-handed people?

In this notebook, we explore the phenomenon of left-handedness and its correlation with age at death. Using age distribution data, we aim to determine if there is a significant difference in the average age at death between left-handed and right-handed individuals. The analysis utilizes Bayesian statistics and pandas to examine the probability of being a certain age at death based on handedness.

A National Geographic survey conducted in 1986 provided valuable data on age, sex, and hand preference for a large sample. Researchers Avery Gilbert and Charles Wysocki observed a decline in left-handedness rates with age, attributing it to changing social acceptability rather than age itself. We will investigate this trend and its implications.


## 2. Rates of left-handedness over time

We convert the data to display the rates of left-handedness as a function of the birth year, averaging over male and female rates. This allows us to understand how left-handedness rates have evolved over time since the study was conducted in 1986.


### 3. Applying Bayes' rule

Bayes' theorem is applied to calculate the probability of dying at a certain age given left-handedness (P(A | LH)) and right-handedness (P(A | RH)). This involves considering conditional probabilities and updating beliefs based on evidence.


### 4. When do people normally die?

We estimate the probability distribution of ages at death using death distribution data for the United States in 1999. This distribution will serve as a baseline for comparing ages at death for left-handed and right-handed individuals.


## 5. The overall probability of left-handedness

We calculate the overall probability of being left-handed (P(LH)) in the population of deceased individuals. This involves summing up left-handedness probabilities for each age, weighted by the number of deceased people at each age.


## 6. Putting it all together: dying while left-handed (i)

We combine probabilities to calculate P(A | LH), the probability of being a particular age at death given left-handedness, using Bayes' rule.


## 7. Putting it all together: dying while left-handed (ii)

We repeat the calculation for right-handed individuals to obtain P(A | RH), the probability of being a particular age at death given right-handedness.


## 8. Plotting the distributions of conditional probabilities

We visualize the distributions of conditional probabilities for both left-handed and right-handed individuals across a range of ages at death.


## 9. Moment of truth: age of left and right-handers at death

We calculate the average ages at death for left-handed and right-handed individuals based on the probability distributions.


## 10. Final comments

We discuss the results, considering factors that may impact the age gap between left-handed and right-handed individuals. Additionally, we explore the expected age gap in 2018, reflecting the changing landscape of left-handedness rates over time.

The analysis provides insights into the relationship between handedness and age at death, debunking the notion that left-handed individuals die younger. The results are based on available data and assumptions, acknowledging potential variations due to sample size, study year, and regional differences.


## Additional Insights

### Limitations and Considerations

- **Data Sources:** The analysis relies on specific datasets, and any limitations or biases in these sources could affect the results.
  
- **Temporal Factors:** The study primarily focuses on data from the 1986 National Geographic survey and death distribution data from 1999. Changes in societal attitudes and behaviors over time may influence the observed trends.

- **Geographical Variations:** The death distribution data cover the entire United States. Variations in left-handedness rates and average ages at death may exist across different regions.

### Future Directions

- **Extended Analysis:** Further exploration could involve analyzing more recent data to observe any shifts in left-handedness rates and their impact on average ages at death.

- **Geographical Specifics:** Conducting similar analyses on a regional level, considering factors like cultural differences and regional variations in left-handedness rates.

- **Statistical Robustness:** Performing sensitivity analyses and incorporating statistical measures of uncertainty to enhance the robustness of the findings.

### Conclusion

The analysis sheds light on the intricate relationship between handedness and age at death, emphasizing the importance of considering social factors in interpreting such trends. While the results challenge the stereotype of left-handed individuals having shorter lifespans, continuous research and exploration are crucial for a comprehensive understanding of these phenomena.

---
