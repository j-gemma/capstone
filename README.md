This project is still a work in progress

Replication of the academic paper called "Automatic Design of Sound Synthesizers as Pure Data Patches Using Coevolutionary Mixed Type Cartesian Genetic Programming"

A brief explanation:

Input a waveform file (.WAV) and this program will output a Pure Data patch (.pd) which is the MT-CGP's best attempt at recreating exactly the input waveform. 

This works using two processes: 

1. Genetic algorithm: Evovlve a population of input parameters.

2. Genetic programming: Evovlve a population of synthesizers which are pure data patches.

These processes use one fitness function which takes a given pure data patch, represented as an acyclic graph in our program, and an instance of input parameters. 
The fitness function measures how closely the graph (synthesizer) with its input parameters matches or does not match the input waveform. 

Populations are evolved for 'n' generations or until a fitness of 1 is achieved (the generated pure data patch outputs exactly the input waveform).

More here soon - my biggest hurdle was learning pyke, the logic tool used to deduce the working pure data patch from a randomly generated graph - which is mostly done.

Next step is automation for turning the deduced graph into a working .pd file so that output can be processed and given to the fitness function for any graph generated.
