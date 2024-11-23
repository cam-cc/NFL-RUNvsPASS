# python script 
import pandas as pd
import glob

def get_motion_features(plays_df):
    """
    Combine all tracking_week_*.csv files into one dataframe. Keep only the BEFORE_SNAP frames. 
    Keep only the last 10 frames before the snap. Calculate the number of players with significant 
    movement (speed > 0.62) for each play. Add this as a feature to the plays dataframe.
    """
    # Keep track of our target plays
    valid_plays = plays_df[['gameId', 'playId']].copy()
    all_motion = []
    
    for file in sorted(glob.glob('tracking_week_*.csv')):
        df = pd.read_csv(file)
        df = df[df['frameType'] == 'BEFORE_SNAP']
    
        # Get last 10 frames before snap for each play
        df = df.groupby(['gameId', 'playId']).tail(10)
        
        motion_features = df.groupby(['gameId', 'playId']).agg({
            's': lambda x: (x > 0.62).sum(),  # Count frames with significant movement
            'x': lambda x: x.max() - x.min(),  # Total lateral movement
        }).reset_index()
        
        all_motion.append(motion_features)
        print(f"Processed {file}: {len(motion_features)} plays")
        
    return pd.concat(all_motion)