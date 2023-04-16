#uploadding my progress but no matter what i do i cannot for the life of me avoid getting the model i attempt to create to not kill itself due to computational power needed
even when using only commentsmarch2018.csv i still end up with my program killing itself.
i will in the upcoming break fix this issue...


#update1
i have now tried lowering batch size, epochs and max_len to 100. still getting error.
will try to lower max_len and other parameters further, still only working with 1 commentsmarch2018.csv

#update2 
max_len 50 allows me to continue on from sequence forming, but still crashes when trying to create model. will change more variables
lowering batch_size to 16 in the create model function and the epoch to 50 in hopes that this will significantly lower cpu usage.
still crashing even with massivly lowered restrictions, unsure what to change.

#tried using the fastest avaialble machine on ucloud and both running through normal scripts and a jupiter notebook, having same error on both.