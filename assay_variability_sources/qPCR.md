*qPCR measures the Ct value of a sample. The Ct value is the number of PCR cycles required to reach a standard fluorescence threshold using fluorescent probes. A Ct of **37** is roughly equivalent to starting with a single copy. A lower Ct value indicates that there was more starting DNA.*

---

## Sources of variability in Ct value: 


### Quantity of starting DNA:
    Signal: Concentration between samples varies because the copy number in the cell lysate varies.

    Noise: Copy number varies because of pipetting mistakes, dilution math errors, contamination, etc.

### Exponential Phase Efficiency (factor by which DNA quantity increases each cycle):
    Noise: If EPE is lower than 2 due to poor primer design, poorly chosen cycle setting, etc. then Ct values will be artificially inflated. It is possible to calibrate for a lower EPE, so this is not always a huge problem.

### Baseline signal:
    Noise: The baseline is established while PCR is in early stages and too dilute to fluoresce. An inaccurate baseline
    would result in wonky Ct values.