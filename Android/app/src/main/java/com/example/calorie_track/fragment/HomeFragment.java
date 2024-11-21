package com.example.calorie_track.fragment;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import com.bumptech.glide.Glide;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.calorie_track.R;
import com.example.calorie_track.data.CalorieInfo;
import com.example.calorie_track.service.CalorieService;
import com.example.calorie_track.util.Constant;
import com.example.calorie_track.util.RetrofitClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HomeFragment extends Fragment {
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_home, container, false);

        ImageView calorieGraphImageView = root.findViewById(R.id.calorieGraphImageView);
        TextView calorieIntake=root.findViewById(R.id.calorieIntake);
        TextView calorieConsumption=root.findViewById(R.id.calorieConsumption);
        String imageUrl = Constant.FLASK_BASE_URL+"calorie_graph";  // Use your server IP address
        Glide.with(this)
                .load(imageUrl)
                .into(calorieGraphImageView);
        CalorieService calorieService = RetrofitClient.getInstance().create(CalorieService.class);

        Call<CalorieInfo> call = calorieService.getCalorieInfo();
        call.enqueue(new Callback<CalorieInfo>() {
            @Override
            public void onResponse(Call<CalorieInfo> call, Response<CalorieInfo> response) {
                if (response.isSuccessful() && response.body() != null) {
                    CalorieInfo data = response.body();
                    Log.d("API_RESPONSE", "Intake: " + data.getIntake() + ", Consumption: " + data.getConsumption());
                    calorieIntake.setText(String.valueOf(data.getIntake())+" cal");
                    calorieConsumption.setText(String.valueOf(data.getConsumption())+" cal");
                } else {
                    Log.e("API_ERROR", "Response unsuccessful or empty");
                }
            }

            @Override
            public void onFailure(Call<CalorieInfo> call, Throwable t) {
                Log.e("API_ERROR", "Failed to fetch data", t);
            }
        });

        return root;
    }
}