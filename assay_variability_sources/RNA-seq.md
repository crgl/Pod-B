# RNA Seq What could go wrong!

Several real categories of error/variability/error types:
- Contamination
- Over Expression
- Preparation
- Reagent issues

## Let's dive in :)

![RNA Seq](https://microbenotes.com/wp-content/uploads/2022/07/RNA-Sequencing.jpg)

###  Contamination

- Other RNA contamination
    - a common problem in Sequencing analysis
    - if the sample isn't pure you would get different sequences then expected 
    - lowers the efficiency of reads
    - if happens later in the preparation could lead to other issues

https://www.nature.com/articles/s41467-020-15821-9

- DNA contamination
    - same as RNA contamination above
    - workflows for RNA-seq usually require cDNA synthesis
    - DNA reads of the wrong kind/ clouded sequencing output 

- Growth contamination
    - goes without saying?
    - if I have fungus in my DNA the machine will not be happy
    - (Psuedomonas lives in DI water so if it's popsicle it's possible!)

![Fungal](https://images.zapnito.com/cdn-cgi/image/metadata=copyright,format=auto,quality=95,fit=scale-down/https://images.zapnito.com/users/586079/posters/1654602509-28-9058/fa3f4069-020e-4cfb-9ca6-c731009a0cce_large.png)

### Over Expression

#### Cross over with preparation!:
- Multiple PCR rounds
    - too much bio information will overload the machine/your sample
    - At a certain concentration and densities stuff that's weird starts to happen more often?
    - usually the machines can weed out noise like this
    - ex. AACCTTGG binds to ATCCTTGG

https://www.illumina.com/content/dam/illumina/gcs/assembled-assets/marketing-literature/illumina-dna-pcr-free-loading-concentration-tech-note-770-2020-007/illumina-dna-pcr-free-loading-concentration-tech-note-770-2020-007.pdf

#### Biological Variety
- Cross-Expression
    - not the real term? (maybe)
    - gene product might be influenced by some other transcription factor
    - provide elevated expression in an otherwise normal scenario
    - ex. TNF Traf-6 pathway and Nf-KB stimulation

- Genetic Expression differences
    - some samples or origins might be different in the propensity to express due to a multitude of factors!
    - persons/place/organism of origin might vary over time due to genetic factors
    - why you thaw new cell types after 30 or so passages


### Preparation

See above for different contaminations!

- inefficient primers
    - much like above you could have the opposite effect too!
    - too little material leads to ineffective and bad data!
    - might compromise the read altogether!

https://pmc.ncbi.nlm.nih.gov/articles/PMC5717752/

- Mis-timing of critical steps!
    - close to home!
    - 5 mins of PCR vs. 10 mins of PCR

### Reagents

- Bad lots of Reagent
    - see contamination
    - measuring and concentration is an issue as well could vary lot to lot

- Mis-Measuring
    - could occur in a number of steps
    - carry over matters a whole lot!
    - resuspension of the primers
    - Volumes of media

- Mis-calculations
    - 2+2=5 type stuff
    - concentration is important to get right!

### The end

# THANK YOU FOR COMING TO MY TED TALK :)

![Fun](https://cdn.myportfolio.com/c5ca24d8c42194c70183b492fb6b1511/44bcf666-c33c-4a26-b72e-d502fb4d1db6_rw_1920.jpg?h=14b3b0c995e9c3c50e8d7f3c210393a6)