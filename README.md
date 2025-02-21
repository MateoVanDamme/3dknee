# 3dknee

This project visualizes a CT scan of my knee, processing the original DICOM data obtained from the hospital and converting it to a NRRD file format, which is commonly used for volumetric data. The project hosts a webpage that allows users to visualize the dataset, as well as another example dataset, utilizing volumetric rendering techniques.

The site is live at https://mateovandamme.github.io/3dknee/ (if I didn't mess something up 🤞).  

## Licensing

The CT scan data of my knee is my property and cannot be used in any way. 

The rest of the project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), allowing non-commercial use and sharing with attribution.

## Credit

### Visualization 
The visualization script is based on the [texture3d](https://threejs.org/examples/?q=texture3d#webgl_texture3d) example from Three.js. 

### Datasets

One of the datasets called ``stent.nrrd`` is a 3D volume converted from ``stent.npz`` from the imageio project.
It is a volumetric image showing a stented abdominal aorta. It is in the public domain.

See: https://imageio.readthedocs.io/en/stable/user_guide/standardimages.html
