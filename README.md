# ml-img-project
Machine Learning Image Processing Project (Graduate Course Project)

## Dataset
Dataset can be found here: [geoPose3k dataset](http://cphoto.fit.vutbr.cz/geoPose3K/).  This dataset is called GeoPose3K which contains over three thousand precise camera poses of mountain landscape images. In addition to camera location and orientation, we provide data for the training and evaluation of computer vision methods and applications in the context of outdoor scenes; synthetic depth maps, normal maps, illumination simulation and semantic label (directly from the link).

## Variables 
Variables in the main dataframe, df_gh.csv, come from the individual "info,txt" files that corresponded to each image. All angles are in radians, elevation in meters, and geo-coordinates are in degrees, using WGS84. They are as follows:

  1. **id** -- ordered list of integers to identify each image
  2. **man** -- MANUAL or AUTO. Type of annotation; 1 = MANUAL for manually annotated, 0 = AUTO for annotations estimated automatically using weighted alignment metric.
  3. **ypr** -- YAW, PITCH, ROLL. Camera orientation. Yaw angle is in range (-PI, PI), zero corresponds to the west direction (270 degrees) and increases counter-clockwise. Pitch is in the range (-PI/2, PI/2), with zero at the horizon. Roll is in the range (-PI, PI), with zero indicating a leveled image, and increases for counter-clockwise rotation. 
  4. **lat_e** -- ESTIMATED LATITUDE by BREJCHA Jan and ČADÍK Martin
  5. **long_e** -- ESTIMATED LONGITUDE by BREJCHA Jan and ČADÍK Martin
  6. **elvt_e** -- ESTIMATED ELEVATION by BREJCHA Jan and ČADÍK Martin
  7. **fov_e** -- ESTIMATED FIELD OF VIEW by BREJCHA Jan and ČADÍK Martin
  8. **lat** -- LATITUDE that comes from original photo
  9. **long** -- LONGITUDE that comes from original photo
  10. **elvt** -- ELEVATION accroding to BREJCHA Jan and ČADÍK Martin's digital elevation model at the original lat/long
  11. **fov** -- FIELD OF VIEW that comes from original photo
  12. **yaw** -- YAW angle is in range (-PI, PI), zero corresponds to the west direction (270 degrees) and increases counter-clockwise.
  13. **pitch** -- PITCH is in the range (-PI/2, PI/2), with zero at the horizon.
  14. **roll** -- Roll is in the range (-PI, PI), with zero indicating a leveled image, and increases for counter-clockwise rotation.
  15. **path** -- image path on my computer (removed my path data for sake of github)









Source:
BREJCHA Jan and ČADÍK Martin. GeoPose3K: Mountain Landscape Dataset for Camera 
Pose Estimation in Outdoor Environments. Image and Vision Computing. 
Washington: Elsevier Science, 2017, ISSN 1433-7541, doi: 10.1016/j.imavis.2017.05.009


         
