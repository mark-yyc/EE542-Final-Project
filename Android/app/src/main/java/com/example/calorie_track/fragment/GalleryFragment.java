package com.example.calorie_track.fragment;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.calorie_track.R;
import com.example.calorie_track.data.CommuteInfo;
import com.example.calorie_track.service.CalorieService;
import com.example.calorie_track.util.Constant;
import com.example.calorie_track.util.RetrofitClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class GalleryFragment extends Fragment {
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_gallery, container, false);
        WebView webView = root.findViewById(R.id.webViewMap);
        webView.setWebViewClient(new WebViewClient()); // Prevent opening in external browser
        webView.getSettings().setJavaScriptEnabled(true); // Enable JavaScript if required

        // Load the map from your backend server
        String mapUrl = Constant.FLASK_BASE_URL+ "map"; // Replace <server_ip> with your server's IP address
        webView.loadUrl(mapUrl);

        TextView distance=root.findViewById(R.id.distance);
        TextView calorieCommute=root.findViewById(R.id.calorieCommute);
        CalorieService calorieService = RetrofitClient.getInstance().create(CalorieService.class);

        Call<CommuteInfo> call = calorieService.getCommuteInfo();
        call.enqueue(new Callback<CommuteInfo>() {
            @Override
            public void onResponse(Call<CommuteInfo> call, Response<CommuteInfo> response) {
                if (response.isSuccessful() && response.body() != null) {
                    CommuteInfo data = response.body();
                    Log.d("API_RESPONSE", "distance: " + data.getDistance() + ", Calorie: " + data.getCalorie());
                    distance.setText("distance: " + data.getDistance() + " m");
                    calorieCommute.setText(data.getCalorie() +" cal");
                } else {
                    Log.e("API_ERROR", "Response unsuccessful or empty");
                }
            }

            @Override
            public void onFailure(Call<CommuteInfo> call, Throwable t) {
                Log.e("API_ERROR", "Failed to fetch data", t);
            }
        });
        return root;
    }
}