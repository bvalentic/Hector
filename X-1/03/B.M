% Read all images in a folder
files = dir('*.jpg');
num_images = length(files);

% Define the size to which all images will be resized (e.g., 100x100)
targetSize = [100, 100];

% Preallocate a cell array to hold the resized images
resizedImages = cell(1, num_images);

% Read and resize each image
for i = 1:num_images
    image = imread(files(i).name);
    resizedImages{i} = imresize(image, targetSize);
end

% Concatenate the resized images horizontally
montage = resizedImages{1};
for i = 2:num_images
    montage = [montage, resizedImages{i}];
end

% Plot the montage
imshow(montage);
