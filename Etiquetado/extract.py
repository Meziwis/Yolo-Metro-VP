import av
import os
import yaml
import datetime

def extract_frames(input_path, output_path, fps, start_times, end_times):
    # Open the input video file
    container = av.open(input_path)

    # Create the output directory if it doesn't exist
    video_name = os.path.splitext(os.path.basename(input_path))[0]
    output_dir = os.path.join(output_path, video_name)
    os.makedirs(output_dir, exist_ok=True)

    # Extract frames from the video for each start and end time pair
    for i, (start_time, end_time) in enumerate(zip(start_times, end_times)):
        # Parse the start and end times as datetime.time objects
        try:
            start_time = datetime.datetime.strptime(start_time, "%H:%M:%S").time()
            end_time = datetime.datetime.strptime(end_time, "%H:%M:%S").time()
        except ValueError as e:
            print(f"Error: {e}")
            continue

        # Calculate the start and end frame numbers
        start_frame = int(datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second, microseconds=start_time.microsecond).total_seconds() * container.streams.video[0].average_rate)
        end_frame = int(datetime.timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second, microseconds=end_time.microsecond).total_seconds() * container.streams.video[0].average_rate)

        # Extract frames from the video and save them to the output directory
        for frame_idx, frame in enumerate(container.decode(video=0)):
            if frame_idx < start_frame:
                continue
            if frame_idx > end_frame:
                break
            if frame_idx % int(container.streams.video[0].average_rate / fps) == 0:
                output_filename = os.path.join(output_dir, f"{i}_{frame_idx:06d}.jpg")
                frame.to_image().save(output_filename)

    # Close the input video file
    container.close()

# Load the input YAML file
try:
    with open("input.yaml", "r") as f:
        input_data = yaml.safe_load(f)
except yaml.YAMLError as e:
    print(f"Error: {e}")
    input_data = {}

# Extract frames from each input video
for i, input_path in enumerate(input_data.get("input_paths", [])):
    output_path = input_data.get("output_paths", [])[i]
    fps = input_data.get("fps", [])[i]
    start_time = input_data.get("start_times", [])[i]
    end_time = input_data.get("end_times", [])[i]
    extract_frames(input_path, output_path, fps, start_time, end_time)