# check if the data of county name is unique for each row
pop1.duplicated(['CTYNAME']).any()
pop2.duplicated(['CTYNAME']).any()

# We want to generate the FIP codes for merging in the following steps.
# Add zeros to state and county numbers to fit the format of FIP
pop1['STATE'] = pop1['STATE'].astype(str).str.zfill(2)
pop1['COUNTY'] = pop1['COUNTY'].astype(str).str.zfill(3)
pop1['FIPS'] = pop1['STATE'].map(str) + pop1['COUNTY'].map(str)
pop2['STATE'] = pop2['STATE'].astype(str).str.zfill(2)
pop2['COUNTY'] = pop2['COUNTY'].astype(str).str.zfill(3)
pop2['FIPS'] = pop2['STATE'].map(str) + pop2['COUNTY'].map(str)

# check the duplicates again
pop1.duplicated(['FIPS']).any()
pop2.duplicated(['FIPS']).any()
