import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 1: Load the shapefile ---
# Replace 'path/to/kenya_counties.shp' with your actual path
counties_gdf = gpd.read_file('County.shp')
print(counties_gdf.columns)
print(counties_gdf['COUNTY'].unique())
print(len(counties_gdf['COUNTY'].unique()))

# --- STEP 2: Load your school data ---
# If you already have a DataFrame, skip this part
# Replace 'path/to/school_data.csv' with your actual file
school_df = pd.read_csv('mydata.csv')

# school_df should have at least:
# - County (matching name in shapefile)
# - Schools_Added
# - Final_Percent

# --- STEP 3: Merge them together ---
# Make sure the county names match exactly — otherwise you might need to clean them
merged_gdf = counties_gdf.merge(school_df, left_on='COUNTY', right_on='County')


# --- STEP 4: Plot the map ---
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Color by 'schools_added' column
merged_gdf.plot(column='schools_added',
                cmap='Greens',
                linewidth=0.8,
                edgecolor='0.8',
                legend=True,
                ax=ax)

# Make it look nicer
ax.set_title('Schools Added by County', fontdict={'fontsize': 20})
ax.axis('off')  # Turn off axis

plt.show()


fig, axes = plt.subplots(1, 2, figsize=(18, 12))
# Find the global min and max for the color scale to ensure both maps are on the same scale
vmin = min(merged_gdf['final_percent'].min(), merged_gdf['Gross Enrollment'].min())
vmax = max(merged_gdf['final_percent'].max(), merged_gdf['Gross Enrollment'].max())

# Plot the 'final_percent' heatmap
merged_gdf.plot(column='Gross Enrollment',
        cmap='Greens',
        linewidth=0.8,
        edgecolor='0.8',
        legend=True,
        ax=axes[0],
        vmin=vmin,
        vmax=vmax)
axes[0].set_title('Gross Enrollment Original', fontdict={'fontsize': 20})
axes[0].axis('off')

print(merged_gdf['final_percent'])
# Plot the 'gross_enrollment' heatmap
merged_gdf.plot(column='final_percent',
                cmap='Greens',
                linewidth=0.8,
                edgecolor='0.8',
                legend=True,
                ax=axes[1],
                vmin=vmin,
        vmax=vmax)

# Make it look nicer
axes[1].set_title('Enrollment Post-Intervention', fontdict={'fontsize': 20})
axes[1].axis('off')  # Turn off axis

plt.show()

# Show the plots
plt.tight_layout()
plt.show()
